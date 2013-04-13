from debug_toolbar.panels import DebugPanel
from django.utils.translation import ugettext_lazy as _

style = """
templateviewer.visible {
    display: block !important;
    background: rgba(254, 254, 207, 1) !important;
    margin: 0 !important;
    padding: 0 0 0 5px !important;
    border: 1px solid #222 !important;
    text-align: left !important;
    font-size: 10pt !important;
    line-height: 16px !important;
    font-weight: normal !important;
    color: black !important;
    font: inherit !important;
    vertical-align: baseline !important;
}
"""

script = """
    var jQuery = window.djdt.jQuery;

    jQuery('.djDebugTemplateViewerPanel').click(function(){
        jQuery('templateviewer').toggleClass('visible');
        description = jQuery('.djDebugTemplateViewerPanel small');
        description.toggleClass('isvisible');
        if (description.hasClass('isvisible')) {
            description.text('click to hide');
        } else {
            description.text('click to show');
        }
        return false;
    });
"""


class TemplateViewerPanel(DebugPanel):
    name = 'Template Viewer'
    has_content = True

    def nav_title(self):
        return _('Template Viewer')

    def nav_subtitle(self):
        return 'click to view'

    def title(self):
        return _('Template Viewer')

    def url(self):
        return ''

    def content(self):
        ret = '<script type="text/javascript">' + script + '</script>'
        ret += '<script type="text/javascript">jQuery(\'head\').append(\'<style type="text/css">' + style.replace('\n', '') + '</style>\');</script>'
        return ret
