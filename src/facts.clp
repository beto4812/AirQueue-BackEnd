(deftemplate person
    (slot age)
    (slot sensitivity)
    (slot sex)
)


(deftemplate pollutant
    (slot name)
    (slot value)
)

(deftemplate pollutionLevel
    (slot value)
)

(deftemplate advice
    (slot advice-text)
)


(defrule young
    ?p -> (person (age ?x))

    =>
    (printout t "?p is young " crlf)

)