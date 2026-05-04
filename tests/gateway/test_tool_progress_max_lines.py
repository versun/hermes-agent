from gateway.run import _resolve_tool_progress_max_lines, _trim_tool_progress_lines


def test_tool_progress_trim_keeps_latest_five_lines():
    lines = [f"tool-{i}" for i in range(1, 11)]

    assert _trim_tool_progress_lines(lines, 5) == [
        "tool-6",
        "tool-7",
        "tool-8",
        "tool-9",
        "tool-10",
    ]


def test_tool_progress_trim_leaves_lines_untouched_when_limit_disabled():
    lines = ["tool-1", "tool-2"]

    assert _trim_tool_progress_lines(lines, 0) == lines
    assert _trim_tool_progress_lines(lines, None) == lines


def test_tool_progress_max_lines_prefers_platform_override():
    config = {
        "display": {
            "tool_progress_max_lines": 9,
            "platforms": {
                "telegram": {"tool_progress_max_lines": 5},
            },
        }
    }

    assert _resolve_tool_progress_max_lines(config, "telegram") == 5


def test_tool_progress_max_lines_defaults_to_disabled_for_invalid_values():
    config = {"display": {"platforms": {"telegram": {"tool_progress_max_lines": "junk"}}}}

    assert _resolve_tool_progress_max_lines(config, "telegram") == 0
