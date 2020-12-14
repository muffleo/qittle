def to_camel_case(name: str) -> str:
    return name.split("_")[0] + name.split("_")[1].title()