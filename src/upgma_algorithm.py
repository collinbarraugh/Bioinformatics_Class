import numpy as np

def upgma_iteration(matrix, original, replaced_indices, codes):
    """
    matrix = square matrix input
    original = the first matrix input
    """
    original = np.array(matrix, dtype=float)

    # Convert matrix input to numpy array
    matrix = np.array(matrix, dtype=float)
    dim = matrix.shape

    # Check to make sure matrix size is valid for the algorithm
    assert(dim[0] == dim[1]), "Input is not a square matrix."
    assert(dim[0 != 1]), "Everything is grouped."

    # Find the next shortest pairwise distance and the corresponding indices (groups) in the CURRENT matrix
    current_min = np.max(matrix)
    pair = (-1,-1)
    for r in range(dim[0]):
        for c in range(dim[1]):
            if r <= c: #stay out of upper traingular matix
                continue
            elif current_min > matrix[r,c]:
                current_min = matrix[r,c]
                pair = (r, c) #pair are the indices in the context of the current matrix
    
    #Let's keep track of the groupings
    new_codes = [None] * (len(codes) - 1)
    i = 0
    while i < len(new_codes):
        if i == min(pair):
            new_codes[i] = codes[i] + codes[max(pair)]
            i = i + 1
        elif i >= max(pair):
            new_codes[i] = codes[i+1]
            i = i+1
        else:
            new_codes[i] = codes[i]
            i = i+1

    # Keep track of the number of individuals grouped together that you are about to join
    paired_count1 = len(codes[pair[0]])
    paired_count2 = len(codes[pair[1]])
    
    # Calculate the depth of the new branch
    depth = current_min / 2

    #Take slices
    slice1 = matrix[:, pair[0]]
    slice1[pair[1]] = -1
    slice2 = matrix[:, pair[1]]
    slice2[pair[0]] = -1

    # Calculate the mean pairwise distances with other sequences in new matrix.
    pairwise_mean = sum([slice1*paired_count1, slice2*paired_count2]) / (paired_count1+paired_count2)
    
    if dim[0] > 2:
        # Remove the second occurence of -1
        second_negative_index = np.where(pairwise_mean==-1)[0][1]
        pairwise_mean = np.delete(pairwise_mean, second_negative_index)

        # Construct the new matrix
        index_del = max(pair)
        index_replace = min(pair)
        new_matrix = np.delete(matrix, index_del, axis=0)
        new_matrix = np.delete(new_matrix, index_del, axis=1)

        for i in range(len(pairwise_mean)):
            new_matrix[index_replace,i] = pairwise_mean[i]
            new_matrix[i,index_replace] = pairwise_mean[i]

        new_matrix[new_matrix == 0] = -1
    else:
        new_matrix = np.array([np.max(original)])
        index_replace=0
    
    return {"new_matrix":new_matrix, "depth":depth, "original_matrix": original, "index_replace":index_replace, "new_codes": new_codes}


def upgma_full(matrix, codes):

    original = np.array(matrix, dtype=float)
    current_matrix = np.array(matrix, dtype=float)
    dim = current_matrix.shape[0]
    replaced_indices = []
    groupings_stack = []
    depth_stack = []
    
    while dim > 1:
        iterresults = upgma_iteration(current_matrix, original, replaced_indices, codes)
        replaced_indices.append(iterresults["index_replace"])
        current_matrix = iterresults["new_matrix"]
        groupings_stack.append(codes)
        depth_stack.append(iterresults["depth"])
        codes = iterresults["new_codes"]
        dim = current_matrix.shape[0]

    distances = np.concatenate([np.array([0]), depth_stack])
    last_entry = groupings_stack[-1][0] + groupings_stack[-1][1]
    groupings_stack.append([last_entry])

    return {'groups': groupings_stack, 'depths': distances}

