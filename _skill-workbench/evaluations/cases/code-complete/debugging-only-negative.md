# Diagnose a Reproducible Arithmetic Failure

The failure is deterministic and isolated. The test below fails with `expected 1.5, received 1`. Diagnose the exact root cause and identify the minimal correction. Do not redesign the API, refactor unrelated code, add construction-policy review, or edit files.

```go
func Average(values []int) float64 {
	if len(values) == 0 {
		return 0
	}

	total := 0
	for _, value := range values {
		total += value
	}

	return float64(total / len(values))
}

func TestAverage(t *testing.T) {
	if got := Average([]int{1, 2}); got != 1.5 {
		t.Fatalf("expected 1.5, received %v", got)
	}
}
```
