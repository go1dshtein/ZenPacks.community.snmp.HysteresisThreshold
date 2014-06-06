from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces.template import IRRDDataSourceInfo

from Products.Zuul.interfaces import IInfo, IFacade
from Products.Zuul.interfaces.template import IThresholdInfo


# ZuulMessageFactory is the translation layer. You will see strings intended to
# been seen in the web interface wrapped in _t(). This is so that these strings
# can be automatically translated to other languages.
from Products.Zuul.utils import ZuulMessageFactory as _t

# In Zenoss 3 we mistakenly mapped TextLine to Zope's multi-line text
# equivalent and Text to Zope's single-line text equivalent. This was
# backwards so we flipped their meanings in Zenoss 4. The following block of
# code allows the ZenPack to work properly in Zenoss 3 and 4.

# Until backwards compatibility with Zenoss 3 is no longer desired for your
# ZenPack it is recommended that you use "SingleLineText" and "MultiLineText"
# instead of schema.TextLine or schema.Text.
from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

class IHystThresholdInfo(IThresholdInfo):
    """
    Adapts the HystThreshold Class
    """
    minval = schema.TextLine(title=_t(u'Minimum Value'), order=6)
    maxval = schema.TextLine(title=u'Maximum Value', order=7)
    n = schema.TextLine(title=u'An alert will be raised if N of M measurements failed<br/>Clear event will be generated only after K sequential clear measurements.<br> N', order=12)
    m = schema.TextLine(title=u'M', order=13)
    k = schema.TextLine(title=u'K', order=14)
    escalateCount = schema.Int(title=_t(u'Escalate Count'), order=11)
