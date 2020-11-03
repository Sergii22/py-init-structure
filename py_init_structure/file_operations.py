from yamldirs.filemaker import Filemaker
from py_init_structure.common_components.ui_tests_folders import UITestsFolders as UI
from py_init_structure.common_components.base_files_dir import BaseFileDir as Base
from py_init_structure.common_components.descriptions import Descriptions as DC

Filemaker('/Users/sergii.golovach/environment/py-init-structure/tmp', f"""
    {UI.CONFIGS_DIR.value}:
    - {Base.INIT.value}
    - {UI.CONFIG_FILE.value}: | {DC.CONFIG_EXAMPLE.value}
    {UI.PAGE_OBJECT_DIR.value}:
    - {UI.PAGES_DIR.value}:
        - {Base.INIT.value}
        - {UI.BASE_PAGE.value}: |
            {DC.BASE_PAGE_EXAMPLE.value}
    - {UI.POPUPS_DIR.value}:
        - {Base.INIT.value}
        - {UI.BASE_POPUP.value}: |
            {DC.BASE_POPUP_EXAMPLE.value}
    {UI.TESTS_DIR.value}:
        - {Base.INIT.value}
        - {UI.BASE_TEST.value}: |
            {DC.BASE_TEST.value}
    {UI.TOOLS_FOLDER.value}:
     - {Base.INIT.value}: |
        {DC.TOOLS_DESCRIPTION.value}
""")
