import statistics
import datetime

from django.db.models import Min

from rest_framework.views import APIView
from rest_framework.response import Response

from session.models import Session, Stint, Lap
from circuit.models import Circuit

from metrics.serializers.circuit_summary import CircuitSummarySerializer


class MetricsCircuitSummary(APIView):
    def get(self, request, car_group='gt3', format=None):
        circuits = Circuit.objects.only("id").all()
        summary = []
        for circuit in circuits:
            sessions = Session.objects.only(
                "id").filter(circuit_id=circuit.id,
                             user=request.user,
                             stint__id__isnull=False,
                             car__group=car_group).distinct()
            total_sessions = len(sessions)
            stints = Stint.objects.only('id').filter(
                session_id__in=sessions)

            laps = Lap.objects.filter(
                stint_id__in=stints).order_by("time")[:1000]

            median_time = None
            car = {"name": None, "id": None}
            best_time = None
            session_id = None
            best_lap = None
            total_laps = len(laps)
            new_best = False
            if total_laps > 0:
                best_lap = laps[0]
                median_time = statistics.median([lap.time for lap in laps])
                car = best_lap.stint_id.session_id.car
                best_time = best_lap.time
                session_id = best_lap.stint_id.session_id.id
                best_lap.stint_id.session_id.created_at

                session_date = best_lap.stint_id.session_id.created_at.replace(
                    tzinfo=None)

                time_since_session = datetime.datetime.now() - session_date
                new_best = time_since_session.days < 7

            summary.append({
                "car": car,
                "circuit": circuit,
                "new_best": best_lap,
                "session_id": session_id,
                "best_time": best_time,
                "median_time": median_time,
                "total_sessions": total_sessions,
                "total_laps": total_laps,
            })

        serializer = CircuitSummarySerializer(summary, many=True)
        return Response(serializer.data)
