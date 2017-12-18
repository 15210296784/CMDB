
class RbacMiddleware(object):
    """
    - process_request(self,request)
			- request.path_info    /index/
			- request.session["SESSION_PERMISSION_URL_KEY"]
				[
					/test/
					/login/
					/index/
				]
			- 匹配
			- 成功：
				无
			  失败：
				return HttpResponse('xxx')

			- 登录页面无序任何权限



    """

    pass