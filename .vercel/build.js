let build_app = 1;
let branch_commit = process.env.VERCEL_GIT_COMMIT_REF || '';
let branch_check = process.env.BRANCH_CHECK || branch_commit;
let vercel_env = process.env.VERCEL_ENV || 'preview';
let vercel_lang = process.env.LANGUAGE || 'en';

function isTranslationBranch(name) {
	return name.startsWith('i18n_') || name.startsWith('auto-translate/');
}

// For develop and master branches, always build to make sure everything is updated
if ((vercel_env == 'preview') && (branch_commit != 'develop')) {
	if (vercel_lang == 'en') {
		// English project: skip builds on translation branches
		if (isTranslationBranch(branch_check) || isTranslationBranch(branch_commit)) {
			build_app = 0;
		}
	}
	else {
		build_app = 0;

		// auto-translate/ branches contain all languages — build every language project
		if (branch_commit.startsWith('auto-translate/')) {
			build_app = 1;
		}
		// i18n_ branches: only build if the branch targets this language
		else if (branch_check.startsWith('i18n_') && branch_commit.startsWith('i18n_') && branch_commit.includes(vercel_lang)) {
			if (branch_check && (vercel_env == 'preview')) {
				build_app = 1;
			}
		}
	}
}

process.exit(build_app);
