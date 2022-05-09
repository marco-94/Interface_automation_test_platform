"""
自定义接口返回
"""
from rest_framework.renderers import JSONRenderer


class CustomerRenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            if isinstance(data, dict):
                msg = data.pop('msg', 'success')
                code = data.pop('code', renderer_context["response"].status_code)
            else:
                msg = 'success'
                code = renderer_context["response"].status_code

            ret = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
