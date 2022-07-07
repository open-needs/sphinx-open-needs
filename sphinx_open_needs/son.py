from sphinx_open_needs.version import VERSION


def setup(app):
    # Define SNO variables
    app.add_config_value("on_needs", "", "html", types=[str])

    # Define nodes

    ##################################
    # DIRECTIVES
    ##################################

    # Define directives
    # app.add_directive("on_item", OpenNeedItemDirective)

    ###################################
    # ROLES
    ###################################
    # Provides :need:`ABC_123` for inline links.
    # app.add_role("on_all", XRefRole(nodeclass=OpenNeedRef, innernodeclass=nodes.emphasis, warn_dangling=True))

    ###################################
    # EVENTS
    ###################################
    # Make connections to events
    # Register sphinx-open-needs stuff after it has been initialised.
    app.connect("env-before-read-docs", prepare_env)
    app.connect("source-read", process_per_doc)
    app.connect("doctree-resolved", process_per_doc)
    app.connect("build-finished", process_finish)

    return {
        "version": VERSION,  # identifies the version of our extension
        "parallel_read_safe": True,  # support parallel modes
        "parallel_write_safe": True,
    }


def prepare_env(app, env, _docname):
    pass


def process_per_doc(app, *kwargs):
    pass


def process_finish(app, exception):
    pass
