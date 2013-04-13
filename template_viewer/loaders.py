from django.template.loader import BaseLoader, find_template_loader
import os


class ProxiedTemplateLoader(BaseLoader):
    is_usable = True
    wrapper = (
        u"<templateviewer style='display: none'>{0}</templateviewer>{1}"
    )

    def __init__(self, proxied):
        self.proxy = find_template_loader(proxied).load_template_source

    def load_template_source(self, template_name, template_dirs=None):
        source, origin = self.proxy(template_name, template_dirs=template_dirs)
        relpath = os.path.relpath(origin)
        # Skip debug toolbar templates
        if not '/debug_toolbar/templates/' in origin:
            source = self.wrapper.format(relpath, source)
        return (source, origin)
