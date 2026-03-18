let build_app = 1;
let branch_commit = process.env.VERCEL_GIT_COMMIT_REF || '';
let branch_check = process.env.BRANCH_CHECK || branch_commit;
let vercel_env = process.env.VERCEL_ENV || 'preview';
let vercel_lang = process.env.LANGUAGE || 'en';

function isTranslationBranch(name) {
	return name.startsWith('i18n_') || name.startsWith('auto-translate/');
}

if (vercel_env == 'preview') {
	if (vercel_lang == 'en') {
		// English project: build develop and feature branches, skip translation branches
		if (isTranslationBranch(branch_check) || isTranslationBranch(branch_commit)) {
			build_app = 0;
		}
	}
	else {
		// Language projects: only build on translation branches; skip all other preview builds
		build_app = 0;

		// auto-translate/ branches contain all languages — build every language project
		if (branch_commit.startsWith('auto-translate/')) {
			build_app = 1;
		}
		// i18n_ branches: only build if the branch targets this language
		else if (branch_check.startsWith('i18n_') && branch_commit.startsWith('i18n_') && branch_commit.includes(vercel_lang)) {
			build_app = 1;
		}
	}
}

process.exit(build_app);
