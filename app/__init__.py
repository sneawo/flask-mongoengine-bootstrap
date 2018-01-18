import logging
import logging.config

from structlog import configure, processors, stdlib, threadlocal

logging.basicConfig(level=logging.INFO)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            'format': ('{"level":"%(levelname)s", '
                       '"loggerName":"%(name)s",'
                       '"lineNo":"%(lineno)d",'
                       '"message":"",'
                       '"message_json": %(message)s}')
        }
    },
    'handlers': {
        'json': {
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        }
    },
    'loggers': {
        'app': {
            'handlers': ['json'],
            'propagate': False
        }
    }

})

configure(
    context_class=threadlocal.wrap_dict(dict),
    logger_factory=stdlib.LoggerFactory(),
    wrapper_class=stdlib.BoundLogger,
    processors=[
        stdlib.filter_by_level,
        stdlib.PositionalArgumentsFormatter(),
        processors.StackInfoRenderer(),
        processors.format_exc_info,
        processors.JSONRenderer()]
)
