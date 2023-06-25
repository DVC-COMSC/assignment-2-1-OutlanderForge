def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    male = int(input())
    female = int(input())
    m_perc = 100 * (male / (male+female))
    f_perc = 100 * (female / (male + female))
    print(f"The total number of students: {male + female}")
    print(f"The number of males and females: {male} {female}")
    print(f"The percentage of males and females: {m_perc:.2f} {f_perc:.2f}")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
