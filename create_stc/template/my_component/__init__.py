import os
import streamlit.components.v1 as components

_RELEASE = True
URL = "http://localhost:3001"

if not _RELEASE:
	_component_func = components.declare_component(
	    "my_component",
	    url=URL,
	)
else:
	parent_dir = os.path.dirname(os.path.abspath(__file__))
	build_dir = os.path.join(parent_dir, "frontend/build")
	_component_func = components.declare_component("my_component", path=build_dir)


def my_component(key=None):
	component_value = _component_func(key=key)
	component_name = _component_func.name
	return component_name, component_value