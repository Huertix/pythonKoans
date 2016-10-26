#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1, 1, 1, 5, 1]) => 1150 points
# score([2, 3, 4, 6, 2]) => 0 points
# score([3, 4, 5, 3, 3]) => 350 points
# score([1, 5, 1, 2, 4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.




def score(dice):
    # My Second try
    from collections import Counter
    final_score = 0
    c = Counter(dice)

    for number in c:
        key = number
        value = c[number]

        if key == 1:
            if value >= 3:
                final_score += ( value - 3 ) * 100
                final_score += 1000
            else:
                final_score += value * 100

        elif key == 5:
            if value >= 3:
                final_score += ( value - 3 ) * 50
                final_score += key * 100
            else:
                final_score += value * 50
        else:
            if value >= 3:
                final_score += key * 100

    return final_score


    # Wajid
    # print sorted( [ (key, value) for key, value in  to_dict(dice).iteritems()], key = lambda x : x[1], reverse=True)
    # def to_dict(scores_set):
    #     scores_dict = {}
    #     for score in scores_set:
    #         scores_dict[score] = scores_dict.get(score, 0) + 1
    #     return scores_dict


    # My First try
    # final_score = 0
    # dice_list = list(dice)
    # pending_list = list()
    #
    # while len(dice_list) > 0:
    #     x = dice_list.pop(0)
    #     repeated_list = list()
    #
    #     for y in dice_list:
    #         if x == y:
    #             repeated_list.append(y)
    #
    #     for z in repeated_list: dice_list.remove(z)
    #
    #     if len(repeated_list) > 0:
    #         repeated_list.append(x)
    #         if len(repeated_list) > 3: pending_list.extend(repeated_list[3:])
    #         if len(repeated_list) >= 3:
    #             if 1 in repeated_list:
    #                 final_score += 1000
    #             else:
    #                 final_score += repeated_list.pop(0) * 100
    #
    #         else:
    #             pending_list.extend(repeated_list)
    #     else:
    #         pending_list.append(x)
    #
    # for x in pending_list:
    #     if x == 1:
    #         final_score += 100
    #     elif x == 5:
    #         final_score += 50
    #
    # return final_score


class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1, 5, 5, 1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2, 3, 4, 6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1, 1, 1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2, 2, 2]))
        self.assertEqual(300, score([3, 3, 3]))
        self.assertEqual(400, score([4, 4, 4]))
        self.assertEqual(500, score([5, 5, 5]))
        self.assertEqual(600, score([6, 6, 6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2, 5, 2, 2, 3]))
        self.assertEqual(550, score([5, 5, 5, 5]))
        self.assertEqual(1150, score([1, 1, 1, 5, 1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1, 2, 2, 2]))
        self.assertEqual(350, score([1, 5, 2, 2, 2]))
