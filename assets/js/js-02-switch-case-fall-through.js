function factorial(n) {
    switch (n) {
        case 0:
        case 1:
            return 1;

        default:
            return n * factorial(n-1);
    }
}
