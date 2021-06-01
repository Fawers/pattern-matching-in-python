function factorial(n) {
    switch (n) {
        case 0:
            return 1;

        case 1:
            return 1;

        default:
            return n * factorial(n-1);
    }
}
