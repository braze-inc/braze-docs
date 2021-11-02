let build_app = 1;
let branch_commit = process.env.VERCEL_GIT_COMMIT_REF || '';
let branch_check = process.env.BRANCH_CHECK || '';
let vercel_env = process.env.VERCEL_ENV || 'preview';

// For develop and master branches, always build to make sure everything is updated
if ((vercel_env == 'preview') && (branch_commit != 'develop')) {
	// For staging, check if it's a build from a language branch
	// Cancel if it doesn't match expected branch
	if (branch_check.includes('l10n_') || branch_commit.includes('l10n_')) {
		build_app = 0;
		if (branch_check && (vercel_env == 'preview')) {
			if (branch_commit == branch_check) {
				build_app = 1;
			}
		}
	}
}

process.exit(build_app);
