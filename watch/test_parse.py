from watch import parse

def test_parse():
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe width="560" height="315" src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

test_parse()
