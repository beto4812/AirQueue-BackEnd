(deftemplate person
    (slot age)
    (slot sensitivity) ;low(1) ;medium(2); high (3)
    (slot asthma) ;true; false
    (slot sex)
)

(deftemplate pollutant
    (slot name)
    (slot value)
)

(deftemplate pollutionLevel
    (slot value) ;air quality index
)

(deftemplate advice
    (slot text)
    (slot level); 1; 2; 3 ;keep top level advice
)

;If asthma, trigger high sensitivity by default.

(defrule enjoy_usual_activities_3
    (pollutionLevel {value <= 3})
    =>
    (assert
        (advice (text "Enjoy your usual outdoor activities")
        (level 10)))
)


(defrule consider_reducing_strenuous_activity_4_6
    (person {sensitivity >= 3})
    (pollutionLevel {value >= 4 && value <= 6})
    =>
    (assert
        (advice (text "Consider reducing strenuous physical activity, particularly outdoors")
        (level 20)))
)

(defrule consider_reducing_strenuous_activity_general_7_9
    (person {sensitivity >= 2})
    (pollutionLevel {value >= 7 && value <= 9} )
    =>
    (assert
        (advice (text "If you are experiencing discomfort such as sore eyes, cough or sore throat you should consider reducing activity, particularly outdoors")
        (level 20)))
)

(defrule reduce_strenuous_activity_sensitivity_sensitive_7_9
    (person {sensitivity >= 3})
    (pollutionLevel {value >= 7 && value <= 9} )
    =>
    (assert
        (advice (text "Reduce strenuous physical exertion, particularly outdoors, and particularly if you experience symptoms")
        (level 20)))
)

(defrule reduce_strenuous_activity_elder_7_9
    (person {age >= 65})
    (pollutionLevel {value >= 7 && value <= 9} )
    =>
    (assert
        (advice (text "Reduce physical exertion, particularly outdoors.")
        (level 30)))
)


(defrule reduce_strenuous_general_10
    (pollutionLevel {value >= 10} )
    =>
    (assert
        (advice (text "Reduce strenuous physical exertion, particularly outdoors, and particularly if they experience symptoms")
        (level 20)))
)

(defrule avoid_strenuous_sensitive_10
    (person {sensitivity >= 2})
    (pollutionLevel {value >= 10} )
    =>
    (assert
        (advice (text "Avoid strenuous physical activity.")
        (level 20)))
)

(defquery all-advices
  (advice))