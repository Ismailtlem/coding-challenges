import random
import sys

import click
from sorting_techniques import pysort


@click.group()
@click.version_option()
def cli():
    "sorting-tool like the unix sort tool"


@cli.command(name="sort")
@click.argument("file", type=click.File("r"))
@click.option("-u", "--unique", is_flag=True, help="Get only unique words")
@click.argument("head")
@click.option(
    "-n", "--number", default=1, help="Number of lines to get", type=click.INT
)
@click.option(
    "--sorting-algorithm",
    type=click.Choice(
        ["quick-sort", "random-sort", "merge-sort"], case_sensitive=False
    ),
)
def sort(file, unique, head, sorting_algorithm, number):
    "Command description goes here"

    sort_obj = pysort.Sorting()

    # for line in file.readlines():
    lines = file.readlines()
    print(sorting_algorithm)
    # breakpoint()
    if head:
        sorted_list = (
            sorted(list(set(lines)))[:number] if unique else sorted(lines)[:number]
        )
        if sorting_algorithm == "quick_sort":
            sorted_list = (
                sort_obj.heapSort(list(set(lines)))[:number]
                if unique
                else sort_obj.heapSort(lines)[:number]
            )

        elif sorting_algorithm == "merge_sort":
            sorted_list = (
                sort_obj.mergeSort(list(set(lines)))[:number]
                if unique
                else sort_obj.mergeSort(lines)[:number]
            )

        elif sorting_algorithm == "random_sort":
            uniques_list_element = list(set(lines))
            random_list = (
                random.sample(uniques_list_element, len(uniques_list_element))[:number]
                if unique
                else random.sample(lines, len(lines))[:number]
            )
            return sys.stdout.write("".join(random_list))
        return sys.stdout.write("".join(sorted_list))
    sorted_list = sorted(lines)
    return sys.stdout.write("".join(sorted_list))
