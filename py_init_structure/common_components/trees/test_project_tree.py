from py_init_structure.common_components.test_project_files import TestProjectFiles as TP
from py_init_structure.common_components.base_files_dir import BasePythonFileDir as Base
from py_init_structure.common_components.descriptions import Descriptions as DC


class TesProjectTree:

    @property
    def dir_name(self):
        return self.root_dir_name

    def __init__(self, root_dir_name=None):
        self.root_dir_name = root_dir_name

    @property
    def tree(self):
        return self.tree_dict()

    def tree_dict(self):
        return {
            "name": self.root_dir_name,
            "type": "directory",
            "children": [
                {
                    "name": TP.TOOLS_FOLDER.value,
                    "type": "directory",
                    "children": [
                        {
                            "name": Base.INIT.value,
                            "type": "file",
                            "content": DC.TOOLS_DESCRIPTION.value
                        }
                    ]
                },
                {
                    "name": TP.TESTS_DIR.value,
                    "type": "directory",
                    "children": [
                        {
                            "name": TP.BASE_TEST.value,
                            "type": "file",
                            "content": DC.BASE_TEST.value
                        },
                        {
                            "name": Base.INIT.value,
                            "type": "file"
                        }
                    ]
                },
                {
                    "name": TP.PAGE_OBJECT_DIR.value,
                    "type": "directory",
                    "children": [
                        {
                            "name": TP.POPUPS_DIR.value,
                            "type": "directory",
                            "children": [
                                {
                                    "name": Base.INIT.value,
                                    "type": "file"
                                },
                                {
                                    "name": TP.BASE_POPUP.value,
                                    "type": "file",
                                    "content": DC.BASE_POPUP_EXAMPLE.value
                                }
                            ]
                        },
                        {
                            "name": TP.PAGES_DIR.value,
                            "type": "directory",
                            "children": [
                                {
                                    "name": TP.BASE_PAGE.value,
                                    "type": "file",
                                    "content": DC.BASE_PAGE_EXAMPLE.value
                                },
                                {
                                    "name": Base.INIT.value,
                                    "type": "file"
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": TP.CONFIGS_DIR.value,
                    "type": "directory",
                    "children": [
                        {
                            "name": TP.CONFIG_FILE.value,
                            "type": "file",
                            "content": DC.CONFIG_EXAMPLE.value
                        },
                        {
                            "name": Base.INIT.value,
                            "type": "file"
                        }
                    ]
                },
                {
                    "name": TP.SERVICES_DIR.value,
                    "type": "directory",
                    "children": [
                        {
                            "name": Base.INIT.value,
                            "type": "file"
                        },
                        {
                            "name": TP.BASE_SERVICE.value,
                            "type": "file",
                            "content": DC.BASE_SERVICE_DESCRIPTION.value
                        }
                    ]
                }
            ]
        }
