__version__ = '1.0.0'


def wrap_loaders(loader_lst):
    loader_wrap = 'template_viewer.loaders.ProxiedTemplateLoader'
    return [(loader_wrap, loader_str) for loader_str in loader_lst]
