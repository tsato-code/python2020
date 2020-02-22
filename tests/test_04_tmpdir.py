import os


CONTENT = "content"


def test_tmp_file(tmp_path):
    # tmp_path は pathlib/pathlib2.Path オブジェクト
    # tmp_path ディレクトリ直下に sub ディレクトリ作成
    d = tmp_path / "sub"
    d.mkdir()
    
    # hello.txt を作成して CONTENT を書き込み
    p = d / "hello.txt"
    p.write_text(CONTENT)

    # ファイルを確認
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 0  # => エラー


def test_tmp_dir(tmpdir):
    # tmpdir は py._path.local.LocalPath オブジェクト
    # tmpdir ディレクトリ直下に sub/hello.txt 作成
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")

    # ファイルを確認
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
    assert 0  # => エラー
