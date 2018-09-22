;; There is only one block, A, which is on the table.  A sprayer with
;; red paint is on the table.  Our goal is to have A be red and the
;; arm empty.

(define (problem 0)
  (:domain hw5)
  (:objects A sprayR)
  (:init (arm-empty)
         (block A)
	 (on-table A)
	 (clear A)

	 (sprayer sprayR red)
	 (on-table sprayR)
	 (clear sprayR))
  (:goal (and (arm-empty)
         (color A red))))



