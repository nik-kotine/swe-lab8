import pytest
from rewards_ms.app.config import require_env_variable

def test_RequireEnvVariableShoulRaiseErrorWhenMissing():
    with pytest.raises(RuntimeError):
        require_env_variable("THIS_VARIABLE_DOESNT_EXIST_676767")
