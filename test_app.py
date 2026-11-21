
from app import main


def test_main(capsys):
    main()
    console = capsys.readouterr()
    assert console.out == "Hello, Jenkins!\n"