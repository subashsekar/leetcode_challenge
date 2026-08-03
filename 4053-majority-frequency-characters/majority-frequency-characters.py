from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freq = Counter(s)

        groups = defaultdict(list)

        for ch, f in freq.items():
            groups[f].append(ch)

        best_frequency = max(groups.keys(), key=lambda f: (len(groups[f]), f))

        return "".join(sorted(groups[best_frequency]))