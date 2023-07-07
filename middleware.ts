export function middleware(request: Request, response: Response, next: NextFunction) {

	let isSpider:boolean = !!request.headers['user-agent'].match(/spider/i);

  if (isSpider) {
    request.url = '/blank.html';
  }
	next()
}