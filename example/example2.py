import os
import numpy as np
import logging


def cond_prob_gen(num):
    return [round(np.random.random(), 2) for i in range(num)]


def probjump():
    return np.random.random() < 0.5


def main(logger):

    logger.info("top1")
    if probjump():
        logger.info("p1")
        if probjump():
            logger.info("p1 and p2")
            if probjump():
                logger.info("p1 and p2 and p3")
                if probjump():
                    logger.info("p1 and p2 and p3 and p4")
                    if probjump():
                        logger.info("p1 and p2 and p3 and p4 and p5")
                    else:
                        logger.info("p1 and p2 and p3 and p4 and not p5")
                else:
                    logger.info("p1 and p2 and p3 and not p4")
            else:
                logger.info("p1 and p2 and not p3")
        else:
            logger.info("p1 and not p2")
    else:
        logger.info("not p1")

    logger.info("top2")

    while probjump():
        logger.info("p3")
        if probjump():
            logger.info("p1")
            if probjump():
                logger.info("p1 and p2")
                if probjump():
                    logger.info("p1 and p2 and p3")
                else:
                    logger.info("p1 and p2 and not p3")
            else:
                logger.info("p1 and not p2")
        else:
            logger.info("not p1")
        while probjump():
            logger.info("p4")
            while probjump():
                logger.info("p5")
    logger.info("top3")


if __name__ == "__main__":
    # cond_prob = cond_prob_gen(3)
    # logging.warning(f"{cond_prob=}")
    log_dir = os.path.join("log2")
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s:%(lineno)s] %(message)s")
    for i in range(10000):
        print(f"{i=}")
        fileHandler = logging.FileHandler(os.path.join(log_dir, f"{i}.log"))
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        main(logger)
        logger.removeHandler(fileHandler)
