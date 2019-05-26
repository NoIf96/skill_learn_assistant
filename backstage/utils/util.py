# -*- coding:utf-8 -*-
from utils.data.manager.json.convert_provider import SortConvertProvider


def get_graph_data(skill_list_data, sort_type="sort_major"):
    data = {"nodes": [], "links": [], "categories": []}
    provider = SortConvertProvider()
    options = provider.get_key_value(provider.json_data, sort_type)
    nodes = [
        {
            "category": get_category(skill[sort_type], options),
            "name": skill.name,
            "value": skill.introduction,
            "label": skill.name,
            "symbolSize": get_skill_value(skill) if get_skill_value(skill) > 10 else 10,
            "draggable": True,
            "skill": skill,
        }
        for skill in skill_list_data
    ]
    links = get_links(nodes)
    categories = [{"name": option} for option in options.values()]
    data["nodes"] = nodes
    data["links"] = links
    data["categories"] = categories
    return data


def get_category(serach, options):
    for i, item in enumerate(options.keys()):
        if serach == item:
            return options[item]
    return "-"


def get_skill_value(skill):
    sort_major_mean, sort_secondary_mean, sort_language_mean = get_sort_major_mean()
    value = (
        2 * (int(skill.sort_major) - sort_major_mean)
        + 1.5 * (int(skill.sort_secondary) - sort_secondary_mean)
        + (int(skill.sort_language) - sort_language_mean)
    )
    value /= 3
    return abs(value)


def get_sort_major_mean():
    provider = SortConvertProvider()
    sort_major_options = provider.sort_major
    sort_secondary_options = provider.sort_secondary
    sort_language_options = provider.sort_language
    sort_major_mean = sum(map(int, sort_major_options.keys())) / len(sort_major_options)
    sort_secondary_mean = sum(map(int, sort_secondary_options.keys())) / len(
        sort_secondary_options
    )
    sort_language_mean = sum(map(int, sort_language_options.keys())) / len(
        sort_language_options
    )
    return sort_major_mean, sort_secondary_mean, sort_language_mean


def get_links(nodes):
    links = []
    for i, node_i in enumerate(nodes):
        for j, node_j in enumerate(nodes[i + 1 :]):
            count = 0
            link = {"source": node_i["skill"].name, "target": node_j["skill"].name}
            if node_i["skill"].sort_major == node_j["skill"].sort_major:
                count += 1
            if node_i["skill"].sort_secondary == node_j["skill"].sort_secondary:
                count += 1
            if node_i["skill"].sort_language == node_j["skill"].sort_language:
                count += 2
            if (
                int(node_i["skill"].sort_language)
                <= int(node_j["skill"].sort_language) + 3
            ) and (
                int(node_i["skill"].sort_language)
                >= int(node_j["skill"].sort_language) - 3
            ):
                count += 1
            if count >= 3:
                links.append(link)
    return links
