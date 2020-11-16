from pathlib import Path

import os


class ProjectTree:
    def __init__(self, project_tree, root_dir=None):
        self.project_tree = project_tree
        self.root_dir = root_dir

    def get_tree_representation(self, dir_path: Path, prefix=""):
        """
        Collect directory try representation
        """
        space = '    '
        branch = '│   '
        tee = '├── '
        last = '└── '

        contents = list(dir_path.iterdir())
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if "__pycache__" in path.name:
                continue
            yield prefix + pointer + path.name
            if path.is_dir():
                extension = branch if pointer == tee else space
                yield from \
                    self.get_tree_representation(path,
                                                 prefix=prefix + extension)

    def print_tree(self):
        """
        Print directory tree
        :return:
        """
        for line in self.get_tree_representation(self.root_dir):
            print(line)

    def create_project_tree(self, tree: dict, root_name=None):
        if not root_name:
            root_name = os.getcwd()

        os.makedirs(f"{root_name}", exist_ok=True)
        if tree.get("children"):
            for i in tree.get("children"):
                if i.get("type") == "directory":
                    self.create_project_tree(i, root_name + "/" +
                                             i.get("name"))
                else:
                    with open(os.path.join(root_name,
                                           i.get("name")), 'a') as temp_file:
                        if i.get("content"):
                            temp_file.write(i.get("content"))
                        else:
                            temp_file.write("")
