## Project 2 - recursion
You're working with the Google Drive API. Each resource (e.g. doc, folder, sheet) ' \
   'in Drive is represented via a `ResourceID` (type `int`).

Given a potentially nested file path, like `Odyseus/Engineering/Design/Mocks.pdf`,
you're trying to find the ResourceID for the very last resource within that path, such as `Mocks.pdf` in this example.

However, there's a complication with this.

We have a function called `find_resource_id(resource_name: str, parent_folder_resource_id: str) -> str`
that will call Drive's API to find the ResourceID for the requested name. But you'll notice that it requires that resource's ' \
parent's ID to be known ahead of time in order to work. This means, going back to the example, that to find `Mocks.pdf`'s ID,
we first need to know the ID for the folder `Design`! To find the ID for `Design`,
we first need to know the ID for its parent `Engineering`! And so on. You are, at least,
given the ID for the root folder `Odyseus` (`31`).

Using recursion, implement a function that can find the `ResourceID` for any of the resources in
`Odyseus/Engineering/Design/Mocks.pdf`, e.g. find the ID for `Design` or for `Mocks.pdf`.
This function doesn't need to work for `Odyseus`, because you already know it and you don't have the parent ID for it.

You're given the function `find_resource_id()` as given below. Pretend this isn't hardcoded,
because in the real world this would use Google Drive's API and you woulnd't know the IDs beforehand, beyond the ID for `Odyseus`.

```python
def find_resource_id(resource_name: str, parent_folder_resource_id: int) -> int:
    name_to_id = {
        "Odyseus": 31,
        "Engineering": 94,
        "Design": 17,
        "Mocks.pdf": 55
    }
    if resource_name not in name_to_id:
        raise ValueError(f"Unknown resource name! You inputted {resource_name}")
    name_to_parent = {
        "Engineering": "Odyseus",
        "Design": "Engineering",
        "Mocks.pdf": "Design",
    }
    parent_name = name_to_parent[resource_name]
    if parent_folder_resource_id != name_to_id[parent_name]:
        raise ValueError(f"Invalid parent folder ID! You inputted {parent_folder_resource_id} when the ID for {parent_name} is really {name_to_id[parent_name]}!")
    return name_to_id[resource_name]
```

