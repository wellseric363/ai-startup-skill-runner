from dataclasses import dataclass, field
from typing import Dict, List, Tuple

STAGES: List[Tuple[str, str, str, str]] = [
    ('validate', '验证', '用户是否愿意为痛点付费？', 'yes'),
    ('bp', 'BP', '是否能用一句话说明价值主张？', 'yes'),
    ('policy', '政策', '是否检查数据与合规风险？', 'no'),
    ('pitch', '路演', '是否有 3 分钟 Demo 脚本？', 'yes'),
    ('growth', '获客', '是否有一个低成本获客渠道？', 'yes'),
    ('pricing', '定价', '是否验证过价格锚点？', 'no'),
    ('register', '注册', '是否明确公司/商标注册路径？', 'no'),
]

@dataclass
class SkillRun:
    idea: str
    answers: Dict[str, str] = field(default_factory=dict)

    def score(self) -> int:
        return sum(self._is_pass(self.answers.get(k, d)) for k, _, _, d in STAGES)

    @staticmethod
    def _is_pass(value: str) -> bool:
        return value.strip().lower() in {'yes', 'y', 'true', '1', '是'}

    def report(self) -> str:
        lines = [f'AI Startup Skills: {self.idea}', '-' * 48]
        for key, name, question, default in STAGES:
            answer = self.answers.get(key, default)
            status = 'PASS' if self._is_pass(answer) else 'NEED WORK'
            lines.append(f'[{status:9}] {name}: {question} -> {answer}')
        lines.append('-' * 48)
        lines.append(f'Score: {self.score()}/{len(STAGES)}')
        return '\n'.join(lines)

if __name__ == '__main__':
    idea = 'AI meeting notes for indie founders'
    answers = {
        'validate': 'yes',
        'bp': 'yes',
        'policy': 'no',
        'pitch': 'yes',
        'growth': 'yes',
        'pricing': 'no',
        'register': 'no',
    }
    run = SkillRun(idea, answers)
    print(run.report())
    next_action = '先补齐政策与定价验证，再推进注册。'
    print('Next action:', next_action)
