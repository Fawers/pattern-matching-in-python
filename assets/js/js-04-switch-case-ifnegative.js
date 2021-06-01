function factorial(n) {
    switch (n) {
        case 0:
            return 1;

        case 1:
            return 1;

        default:
            return (n < 0) ? null : n * factorial(n - 1);
            // ou
            if (n < 0) {
                return null;
            }
            else {
                return n * factorial(n-1);
            }
    }
}
