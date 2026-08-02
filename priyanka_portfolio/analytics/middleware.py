from ipware import get_client_ip

from .models import Visitor


class AnalyticsMiddleware:

    COOKIE_NAME = "portfolio_vid"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        visitor = None
        visitor_id = request.COOKIES.get(self.COOKIE_NAME)

        # Existing Visitor
        if visitor_id:
            try:
                visitor = Visitor.objects.get(visitor_id=visitor_id)
            except Visitor.DoesNotExist:
                visitor = None

        # New Visitor
        if visitor is None:

            ip_address, _ = get_client_ip(request)

            user_agent = request.user_agent

            visitor = Visitor.objects.create(
                ip_address=ip_address,
                user_agent=request.META.get("HTTP_USER_AGENT", ""),
                browser=user_agent.browser.family,
                operating_system=user_agent.os.family,
                device=user_agent.device.family or "Desktop",
            )

            request.new_visitor = True

        else:
            request.new_visitor = False

        request.visitor = visitor

        response = self.get_response(request)

        if request.new_visitor:
            response.set_cookie(
                self.COOKIE_NAME,
                str(visitor.visitor_id),
                max_age=60 * 60 * 24 * 365,  # 1 year
                httponly=True,
                samesite="Lax",
            )

        return response