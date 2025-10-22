import pytest
import os
from unittest.mock import patch, mock_open
import main

def test_count_words(capsys):
    main.count_words("this is a small test")
    out = capsys.readouterr().out
    assert "5" in out

def test_open_file(monkeypatch):
    fake_text = "hello this is file"
    m = mock_open(read_data=fake_text)
    with patch("builtins.open", m):
        monkeypatch.setattr("builtins.input", lambda _: "file1")
        result = main.open_file()
        assert result == fake_text

def test_save_output():
    text = "some text"
    with patch("main.open", mock_open()) as m:
        main.save_output(text, "testfile", "txt", "text")
        handle = m()
        handle.write.assert_called_once_with(text)

def test_clear_terminal(monkeypatch):
    called = {}
    def fake_system(cmd):
        called["cmd"] = cmd
    monkeypatch.setattr(os, "system", fake_system)
    main.clear_terminal(0)
    assert called["cmd"] in ["cls", "clear"]

def test_type_effect(capsys):
    main.type_effect("Hi", delay=0)
    out = capsys.readouterr().out
    assert "Hi" in out

def test_print_option(capsys, monkeypatch):
    monkeypatch.setattr("shutil.get_terminal_size", lambda: os.terminal_size((80, 24)))
    main.print_option()
    out = capsys.readouterr().out
    assert "Option" in out

