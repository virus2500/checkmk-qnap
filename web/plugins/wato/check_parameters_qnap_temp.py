group = "checkparams"                                                                                                                                                                                                                        
subgroup_applications = _("Temperature, Humidity, Electrical Parameters, etc.")
register_check_parameters(
    subgroup_applications,
    "qnap_temp",
    _("Parameters for QNAP Temperature"),
    Dictionary(
        elements = [
            ('cpuTemp', Tuple(
                title = _('CPU Temp Thresholds'),
                help = _("Set CPU Thresholds for alarms"),
                elements = [
                    Integer(title = _("Warning at"), unit = _("C"), default_value = 55),
                    Integer(title = _("Critical at"), unit = _("C"), default_value = 60),
                ])),
            ('sysTemp', Tuple(
                title = _('SYS Temp Thresholds'),
                help = _("Set SYS Temp Thresholds for alarms"),
                elements = [
                    Integer(title = _("Warning at"), unit = _("C"), default_value = 55),
                    Integer(title = _("Critical at"), unit = _("C"), default_value = 60),
                ])),
        ],
    ),
    TextAscii(
        title = _("Name of service"),
        allow_empty = False,
    ),
    'dict',
)
