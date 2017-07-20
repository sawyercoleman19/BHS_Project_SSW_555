def US22(IndRef):
	error = []
	if len(IndRef) != len(set(IndRef)):
		for p in IndRef:
			ql = IndRef[0:IndRef.index(p)]+IndRef[IndRef.index(p)+1:]
			for q in ql :
				if p == q :
					error.append(q)

	return set(error)