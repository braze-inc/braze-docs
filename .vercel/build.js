let build_app = 1;
let branch_commit = process.env.VERCEL_GIT_COMMIT_REF || '';
let branch_check = process.env.BRANCH_CHECK || '';
let vercel_env = process.env.VERCEL_ENV || 'preview';
let vercel_lang = process.env.LANGUAGE || 'en';

// For develop and master branches, always build to make sure everything is updated
if ((vercel_env == 'preview') && (branch_commit != 'develop')) {
	// For preview, if language is english project, then don't build if it's an language branch
	// if language is not english, then check if it's a language branch
	if (vercel_lang == 'en') {
		if (branch_check.startsWith('i18n_') || branch_commit.startsWith('i18n_')) {
			build_app = 0;
		}
	}
	else{
		build_app = 0;
		if (branch_check.startsWith('i18n_') && branch_commit.startsWith('i18n_') && branch_commit.includes(vercel_lang)) {
			if (branch_check && (vercel_env == 'preview')) {
				build_app = 1;
			}
		}
	}
}

process.exit(build_app);
