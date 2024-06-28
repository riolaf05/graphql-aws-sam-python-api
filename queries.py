get_appsync_objs = """
query MyQuery {
  getAllNotes {
    id
    date
    extraction
    summary
    title
  }
}
"""

get_appsync_obj = """
query MyQuery {
  getSingleNote(id: "%s") {
    id
    date
    extraction
    summary
    title
  }
}

"""

add_appsync_obj = """
mutation MyMutation {
  createSingleNote(date: "%s", extraction: "%s", summary: "%s", title: "%s") {
    id
  }
}
"""


