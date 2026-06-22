import nox


@nox.session
def docs(session):
    """Build the documentation to static HTML in docs/_build/html."""
    session.install("mystmd")
    session.chdir("docs")
    session.run("myst", "build", "--html")


@nox.session(name="docs-live")
def docs_live(session):
    """Live-preview the documentation with auto-reload."""
    session.install("mystmd")
    session.chdir("docs")
    session.run("myst", "start")
