# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.lib.threaded import ThreadedSegment
from powerline.segments import with_docstring
from kubernetes import config

class K8sClusterInfo(ThreadedSegment):
    interval = 1

    def _update(self):
        context = config.list_kube_config_contexts()[1]['name']
        return context

    def update(self, old):
        return self._update();

    #def run(self):
        #while not self.shutdown_event.is_set():
    #    self.update_value = self._update()
        #    time.sleep(self.interval)


    def render(self, value, **kwargs):
        if "prod" in value:
            color_name = 'k8s_prod'
        else:
            color_name = 'k8s_nonprod'


        return [{'contents': value,
            'highlight_groups': [color_name]}]


k8s_cluster_info = with_docstring(K8sClusterInfo(),
'''Return shit.

Nothing to read.
''')

