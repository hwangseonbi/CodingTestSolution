import pprint
import importlib


def run(problem_id):
    solution_modele_path = ".solutions" + "." + problem_id
    solution_modele = importlib.import_module(
        solution_modele_path, package="programmers")

    testcase_modele_path = ".testcase" + "." + problem_id
    testcase_modele = importlib.import_module(
        testcase_modele_path, package="programmers")

    for i, test_case in enumerate(testcase_modele.TEST_CASES):
        test_case_str = \
            "----------------TEST CASE : #%d---------------\n\
INPUT : %s\n\
---------------------------------------------" % (
                i, pprint.pformat(test_case))
        print(test_case_str)

        testcase_result = test_case.pop("result")
        answer = solution_modele.solution(**test_case)

        print("\n-------------------RESULT--------------------")
        if answer == testcase_result:
            print("pass")
        else:
            print("failed")
            print("- Your answer : %s" % answer)
            print("- Actual answer : %s" % testcase_result)
        print("-------------------END-----------------------")
        print("\n\n\n\n\n\n\n\n")
