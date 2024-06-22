# Espanso Python Utils

A python code snippet package for [Espanso](https://espanso.org/) to reduce boilerplate code.


## Triggers

| Trigger        | Command                                                                                                                                                                                                                                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| :pymain        | <pre>def main() -> None:<br><br>if \_\_name__ == "\_\_main__":<br>    main()</pre>                                                                                                                                                                                                              |
| :pycls         | <pre>class :<br>    def \_\_init__(self) -> None:<br><br><br>    def method_1(self) -> None:<br></pre>                                                                                                                                                                                          |
| :pydef         | <pre>def ():<br><br>    return</pre>                                                                                                                                                                                                                                                            |
| :pymatch       | <pre>match :<br>    case :<br><br>    case _:<br></pre>                                                                                                                                                                                                                                         |
| :pytry         | <pre>try:<br><br>except  as e:<br></pre>                                                                                                                                                                                                                                                        |
| :pyboiler:args | <pre>import argparse<br><br>def main(args: argparse.Namespace) -> None:<br><br>if \_\_name__ == "\_\_main__":<br>    parser = argparse.ArgumentParser()<br><br>    parser.add_argument("")<br><br>    args = parser.parse_args()<br>    main(args)</pre>                                        |
| :pyboiler:log  | <pre>import logging<br><br>logger = logging.getLogger(__name__)<br><br>def main() -> None:<br>    logger.debug("Logger working")<br><br>if \_\_name__ == "\_\_main__":<br>    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(asctime)s: %(message)s")<br><br>    main()</pre> |
