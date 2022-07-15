import os
import numpy as np
import logging


def cond_prob_gen(num):
    return [round(np.random.random(), 2) for i in range(num)]


def probjump(p):
    return np.random.random() < p


def main(cond_prob, logger):
    p1, p2, p3 = cond_prob

    logger.info("top1")
    if probjump(p1):
        logger.info("p1")
        if probjump(p2):
            logger.info("p1 and p2")
        else:
            logger.info("p1 and not p2")
    else:
        logger.info("not p1")

    logger.info("top2")

    while probjump(p3):
        logger.info("p3")

    logger.info("top3")


if __name__ == "__main__":
    cond_prob = cond_prob_gen(3)
    logging.warning(f"{cond_prob=}")
    log_dir = os.path.join(
        "log", "-".join([str(int(p * 100)) for p in cond_prob])
    )
    os.makedirs(log_dir, exist_ok=True)
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s:%(lineno)s] %(message)s")
    for i in range(10000):
        print(f"{i=}")
        fileHandler = logging.FileHandler(os.path.join(log_dir, f"{i}.log"))
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        main(cond_prob, logger)
        logger.removeHandler(fileHandler)
