# This file is automatically generated by gendoc

from . import server, _server
@server.serializable_type('anvil.Component')
class Component(_server.SerializeWithIdentity):
    def __init__(self,__ignore_property_exceptions=False,**props):
        self.__dict__.update(props)
    def __deserialize__(self, data, global_data):
        self.__dict__.update(data)
    def __serialize_once__(self, global_data):
        return self.__dict__

@server.serializable_type('anvil.Container')
class Container(Component):
    def __init__(self,__ignore_property_exceptions=False,**props):
        self.__dict__['$_components'] = []
        self.__dict__.update(props)
    def add_component(self, c, **lp):
        self.__dict__['$_components'].append((c, lp))

@server.serializable_type('anvil.ComponentTag')
class ComponentTag(object):
    pass

@server.serializable_type('anvil.Button')
class Button(Component):
    pass

@server.serializable_type('anvil.Canvas')
class Canvas(Component):
    pass

@server.serializable_type('anvil.CheckBox')
class CheckBox(Component):
    pass

@server.serializable_type('anvil.ColumnPanel')
class ColumnPanel(Container):
    pass

@server.serializable_type('anvil.DataGrid')
class DataGrid(Container):
    pass

@server.serializable_type('anvil.DataRowPanel')
class DataRowPanel(Container):
    pass

@server.serializable_type('anvil.DatePicker')
class DatePicker(Component):
    pass

@server.serializable_type('anvil.DropDown')
class DropDown(Component):
    pass

@server.serializable_type('anvil.FileLoader')
class FileLoader(Component):
    pass

@server.serializable_type('anvil.FlowPanel')
class FlowPanel(Container):
    pass

@server.serializable_type('anvil.GoogleMap')
class GoogleMap(Container):
    pass

@server.serializable_type('anvil.GridPanel')
class GridPanel(Container):
    pass

@server.serializable_type('anvil.HtmlTemplate')
class HtmlTemplate(Container):
    pass

@server.serializable_type('anvil.Image')
class Image(Component):
    pass

@server.serializable_type('anvil.Label')
class Label(Component):
    pass

@server.serializable_type('anvil.LinearPanel')
class LinearPanel(Container):
    pass

@server.serializable_type('anvil.Link')
class Link(Container):
    pass

@server.serializable_type('anvil.Plot')
class Plot(Component):
    pass

@server.serializable_type('anvil.RadioButton')
class RadioButton(Component):
    pass

@server.serializable_type('anvil.RepeatingPanel')
class RepeatingPanel(Component):
    pass

@server.serializable_type('anvil.Spacer')
class Spacer(Component):
    pass

@server.serializable_type('anvil.TextArea')
class TextArea(Component):
    pass

@server.serializable_type('anvil.TextBox')
class TextBox(Component):
    pass

@server.serializable_type('anvil.Timer')
class Timer(Component):
    pass

@server.serializable_type('anvil.XYPanel')
class XYPanel(Container):
    pass

@server.serializable_type('anvil.YouTubeVideo')
class YouTubeVideo(Component):
    pass

