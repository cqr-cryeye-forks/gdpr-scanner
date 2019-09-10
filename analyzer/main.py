"""
Main entry of the package
"""
import logging
import os

from analyzer.analyze import Analyzer


def main():
    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s:%(name)s %(message)s',
        # filename='app.log',
        # filemode='w',
    )

    # Start analyzer
    # ToDo Command line args?

    main_dir = os.path.dirname(os.path.realpath(__file__))
    analyzer = Analyzer(crawler_metadata_filepath=os.path.join(main_dir, '../output/crawler.json'))
    analyzer.run()


if __name__ == '__main__':
    main()