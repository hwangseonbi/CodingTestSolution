import pprint
import importlib


def run(problem_id):
    solution_modele_path = ".solutions" + "." + problem_id
    solution_modele = importlib.import_module(
        solution_modele_path, package="baekjoon")

    testcase_modele_path = ".testcase" + "." + problem_id
    testcase_modele = importlib.import_module(
        testcase_modele_path, package="baekjoon")

    for i, test_case in enumerate(testcase_modele.TEST_CASES):
        test_case_str = \
            "----------------TEST CASE : #%d---------------\n\
INPUT : %s\n\
---------------------------------------------" % (
                i, pprint.pformat(test_case))
        print(test_case_str)

        testcase_output = test_case.pop("output")
        answer = solution_modele.input_from_str(**test_case)

        print("\n-------------------RESULT--------------------")
        if answer == testcase_output:
            print("pass")
        else:
            print("failed")
            print("- Your answer : %s" % answer)
            print("- Actual answer : %s" % testcase_output)
        print("-------------------END-----------------------")
        print("\n\n")
