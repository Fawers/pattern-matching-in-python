function factorial(n) {
    switch (n) {
        case -2:
        case -1:
        case 0:
        case 1:
            return 1;

        default:
            return n * factorial(n-1);
    }
}
