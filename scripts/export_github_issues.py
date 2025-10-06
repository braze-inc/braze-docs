#!/usr/bin/env python3
"""
Script to export all GitHub issues from a repository to CSV format.
"""

import requests
import csv
import json
import os
from datetime import datetime, timedelta
import time

def get_repo_info():
    """Get repository information from git remote."""
    try:
        import subprocess
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                              capture_output=True, text=True, check=True)
        remote_url = result.stdout.strip()
        
        # Parse GitHub URL to get owner and repo
        if 'github.com' in remote_url:
            if remote_url.startswith('git@'):
                # SSH format: git@github.com:owner/repo.git
                parts = remote_url.replace('git@github.com:', '').replace('.git', '').split('/')
            else:
                # HTTPS format: https://github.com/owner/repo.git
                parts = remote_url.replace('https://github.com/', '').replace('.git', '').split('/')
            
            if len(parts) >= 2:
                return parts[0], parts[1]
    except Exception as e:
        print(f"Error getting repo info: {e}")
    
    return None, None

def fetch_all_issues(owner, repo, token=None):
    """Fetch all issues from GitHub repository created or updated in the past 3 months."""
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'GitHub-Issues-Exporter'
    }
    
    if token:
        headers['Authorization'] = f'token {token}'
    
    # Calculate date 3 months ago
    three_months_ago = datetime.now() - timedelta(days=90)
    since_date = three_months_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
    
    all_issues = []
    page = 1
    per_page = 100
    
    print(f"Fetching issues from {owner}/{repo} since {since_date}...")
    
    while True:
        url = f'https://api.github.com/repos/{owner}/{repo}/issues'
        params = {
            'state': 'all',  # Get both open and closed issues
            'page': page,
            'per_page': per_page,
            'sort': 'updated',  # Sort by updated to catch recently modified issues
            'direction': 'desc',
            'since': since_date  # Only get issues updated since 3 months ago
        }
        
        print(f"Fetching page {page}...")
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 403:
            print("Rate limit exceeded. Waiting 60 seconds...")
            time.sleep(60)
            continue
        elif response.status_code != 200:
            print(f"Error fetching issues: {response.status_code}")
            print(response.text)
            break
        
        issues = response.json()
        
        if not issues:
            break
        
        # Filter out pull requests (GitHub API includes PRs in issues endpoint)
        issues = [issue for issue in issues if 'pull_request' not in issue]
        
        # Additional filtering: only include issues created or updated in the past 3 months
        filtered_issues = []
        for issue in issues:
            created_date = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            updated_date = datetime.strptime(issue['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
            
            # Include if created OR updated in the past 3 months
            if created_date >= three_months_ago or updated_date >= three_months_ago:
                filtered_issues.append(issue)
            else:
                # If we've reached issues older than 3 months, we can stop
                # (since we're sorting by updated date descending)
                print(f"Reached issues older than 3 months, stopping...")
                break
        
        all_issues.extend(filtered_issues)
        print(f"Fetched {len(filtered_issues)} relevant issues from page {page}")
        
        # If we got fewer filtered issues than the page size, we've likely reached the cutoff
        if len(filtered_issues) < len(issues) or len(issues) < per_page:
            break
        
        page += 1
        time.sleep(1)  # Be nice to the API
    
    return all_issues

def export_to_csv(issues, filename):
    """Export issues to CSV file."""
    if not issues:
        print("No issues to export.")
        return
    
    fieldnames = [
        'number',
        'title',
        'state',
        'created_at',
        'updated_at',
        'closed_at',
        'author',
        'assignees',
        'labels',
        'milestone',
        'comments_count',
        'body',
        'url'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for issue in issues:
            # Extract assignees
            assignees = ', '.join([assignee['login'] for assignee in issue.get('assignees', [])])
            
            # Extract labels
            labels = ', '.join([label['name'] for label in issue.get('labels', [])])
            
            # Extract milestone
            milestone = issue.get('milestone', {}).get('title', '') if issue.get('milestone') else ''
            
            # Convert date strings to datetime objects (ISO 8601 format)
            created_at = datetime.strptime(issue['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
            updated_at = datetime.strptime(issue['updated_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
            closed_at = datetime.strptime(issue['closed_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S') if issue.get('closed_at') else ''
            
            row = {
                'number': issue['number'],
                'title': issue['title'],
                'state': issue['state'],
                'created_at': created_at,
                'updated_at': updated_at,
                'closed_at': closed_at,
                'author': issue['user']['login'],
                'assignees': assignees,
                'labels': labels,
                'milestone': milestone,
                'comments_count': issue['comments'],
                'body': issue.get('body', '').replace('\n', ' ').replace('\r', ' ') if issue.get('body') else '',
                'url': issue['html_url']
            }
            writer.writerow(row)
    
    print(f"Exported {len(issues)} issues to {filename}")

def main():
    # Get repository information
    owner, repo = get_repo_info()
    
    if not owner or not repo:
        print("Could not determine repository information.")
        print("Make sure you're in a git repository with a GitHub remote.")
        return
    
    print(f"Repository: {owner}/{repo}")
    
    # Check for GitHub token in environment
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Warning: No GITHUB_TOKEN environment variable found.")
        print("You may hit rate limits. Consider setting a GitHub personal access token.")
        print("Export GITHUB_TOKEN=your_token_here")
    
    # Fetch all issues
    issues = fetch_all_issues(owner, repo, token)
    
    # Export to CSV
    filename = 'issues-export-10-03.csv'
    export_to_csv(issues, filename)
    
    print(f"\nExport complete!")
    print(f"File: {filename}")
    print(f"Total issues exported (past 3 months): {len(issues)}")

if __name__ == '__main__':
    main()
