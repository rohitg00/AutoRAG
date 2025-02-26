import pytest

from autorag.nodes.passagereranker import FlashRankReranker
from tests.autorag.nodes.passagereranker.test_passage_reranker_base import (
	base_reranker_test,
	base_reranker_node_test,
	queries_example,
	contents_example,
	ids_example,
	project_dir,
	previous_result,
)
from tests.delete_tests import is_github_action


@pytest.fixture
def flashrank_instance():
	return FlashRankReranker(project_dir, "ms-marco-TinyBERT-L-2-v2")


@pytest.mark.skipif(is_github_action(), reason="Skipping this test on GitHub Actions")
def test_flashrank_reranker(flashrank_instance):
	top_k = 1
	contents_result, id_result, score_result = flashrank_instance._pure(
		queries_example, contents_example, ids_example, top_k
	)
	base_reranker_test(contents_result, id_result, score_result, top_k)


@pytest.mark.skipif(is_github_action(), reason="Skipping this test on GitHub Actions")
def test_flashrank_reranker_batch_one(flashrank_instance):
	top_k = 1
	batch = 1
	contents_result, id_result, score_result = flashrank_instance._pure(
		queries_example,
		contents_example,
		ids_example,
		top_k,
		batch=batch,
	)
	base_reranker_test(contents_result, id_result, score_result, top_k)


@pytest.mark.skipif(is_github_action(), reason="Skipping this test on GitHub Actions")
def test_flashrank_reranker_node():
	top_k = 1
	result_df = FlashRankReranker.run_evaluator(
		project_dir=project_dir, previous_result=previous_result, top_k=top_k
	)
	base_reranker_node_test(result_df, top_k)
